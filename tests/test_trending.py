from TikTokApi import TikTokApi
import os
import pytest

ms_token = os.environ.get("ms_token", None)


@pytest.mark.asyncio
async def test_trending():
    api = TikTokApi()
    async with api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3, browser=os.getenv("TIKTOK_BROWSER", "chromium"))
        count = 0
        async for video in api.trending.videos(count=100):
            count += 1

        assert count >= 100
