import os
import time
from typing import Any, Dict, Optional
import httpx
from dotenv import load_dotenv

load_dotenv()  # 必须显式调用这一行，否则 .env 不会生效

class BangumiClient:
    """Bangumi API v0 工程化客户端封装。"""

    BASE_URL = "https://api.bgm.tv/v0"

    def __init__(self, access_token: Optional[str] = None, app_id: str = "Narrarch/bgm-research/1.0"):
        # 优先从参数读取，否则从系统环境变量安全加载
        self.token = access_token or os.getenv("BGM_ACCESS_TOKEN")
        if not self.token:
            raise ValueError("Missing BGM_ACCESS_TOKEN. Please set it in environment variables.")

        # 构造全局默认请求头契约
        default_headers = {
            "Authorization": f"Bearer {self.token}",
            "User-Agent": app_id,
            "Accept": "application/json",
        }

        # 初始化底层连接池会话，统一管理超时与请求头
        self._client = httpx.Client(
            base_url=self.BASE_URL,
            headers=default_headers,
            timeout=httpx.Timeout(10.0, connect=5.0),
        )

    def get_subject(self, subject_id: int) -> Dict[str, Any]:
        """获取指定条目（番剧/书籍/游戏）的完整元数据。"""
        response = self._client.get(f"/subjects/{subject_id}")
        # 若状态码为 4xx/5xx（如 401 Token失效、404 条目不存在、429 触发限流），直接抛出异常
        response.raise_for_status()
        return response.json()

    def search_subjects(self, keyword: str, subject_type: int = 2, limit: int = 10) -> Dict[str, Any]:
        """按条件检索条目（POST 请求示例，subject_type=2 代表动画）。"""
        payload = {
            "keyword": keyword,
            "filter": {"type": [subject_type]},
        }
        # params 控制 URL 查询参数，json 自动序列化请求体并注入 Content-Type: application/json
        response = self._client.post("/search/subjects", params={"limit": limit}, json=payload)
        response.raise_for_status()
        return response.json()

    def close(self) -> None:
        """显式释放底层 TCP 连接池资源。"""
        self._client.close()

    def __enter__(self) -> "BangumiClient":
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.close()


# --- 实战调用验证 ---
if __name__ == "__main__":
    # 衔接你在 Py.22/Py.28 练过的上下文管理器协议（Context Manager）
    with BangumiClient() as client:
        # 1. 验证个人鉴权是否生效（获取当前 Token 绑定的用户信息）
        me = client._client.get("/me").json()
        print(f"鉴权成功，当前身份: {me.get('nickname')} (@{me.get('username')})")

        # 2. 抓取具体条目（例如：ID 253 为《钢之炼金术师 FULLMETAL ALCHEMIST》）
        data = client.get_subject(25)
        print(f"条目名称: {data.get('name_cn')} | 评分: {data.get('rating', {}).get('score')}")

        # TODO: 在这里设计你的批量调度与速率控制（Rate Limiting）逻辑