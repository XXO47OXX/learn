import requests
import json
from concurrent.futures import ThreadPoolExecutor

payload = {}
headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6bnVsbCwidWlkIjoyMDM2OTk0MTMzLCJzdWIiOiJlMGEzNTljZi1hN2Y4LTQxNDAtYTdjZC02MjhhYjk2NDFkYmYiLCJyb2xlcyI6MCwiaWF0IjoxNjc5NTQ5MjI2fQ.vUkWnOEiw_c1tAstkG3OoTS_z-I76Qd2Z4Gi9cN67UU',
    'Connection': 'keep-alive',
    'Origin': 'https://5a2f.tianliplanner.com',
    'Referer': 'https://5a2f.tianliplanner.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    'content-type': 'application/json; charset=utf-8',
    'Cookie': 'acw_tc=a3b546a816795500399001430e0a8aa7a86dd253bb94e26befefb5178e; cdn_sec_tc=a3b546a816795500399001430e0a8aa7a86dd253bb94e26befefb5178e'
}


# CATEGORY_IDS = [272, 234, 112, 117, 231, 238, 233, 240, 114, 233, 270, 197]
CATEGORY_IDS = [234]
VIDEO_DICT = {}


# def get_video_by_category(catagory_id, page, video_dict):
#     try:
#         url = f"https://api.tianliplanner.com/public/internalTags/internalTag/views?page={page}&limit=100&internalTagId={catagory_id}"
#         response = requests.request(
#             "GET", url, headers=headers, data=payload)
#         results = json.loads(response.text)
#         data_list = results['data']
#         for data in data_list:
#             if data.get('id') not in video_dict:
#                 video_dict.append(data.get('id'))
#     except Exception as e:
#         pass


def get_content(i, video_ids):
    url = f"https://api.tianliplanner.com/public/videos/video/videoUrl?id={i}"
    video_detail = f'https://api.tianliplanner.com/public/videos/video/videoDetail?id={i}'
    try:
        response = requests.request(
            "GET", url, headers=headers, data=payload)
        if response.status_code !=200:
            raise response.status_code
        
        results = json.loads(response.text)
        video_url = results['data']['videoUrl']
        title = results['data']['title']
        video_url = video_url.split("\\")[-1]
        video_url = f"https://cdn.jianlimy.com/{video_url}/{video_url}.m3u8"
        response_detail = requests.request(
            "GET", video_detail, headers=headers, data=payload)
        if response_detail.status_code !=200:
            raise response.status_code
        results_detail = json.loads(response_detail.text)
        tags = results_detail['data']['internalTag']
        for tag in tags:
            if tag in CATEGORY_IDS:
                video_ids.append(f"{title} : {video_url}\n")
    except Exception as e:
        pass


# for category_id in CATEGORY_IDS:
#     VIDEO_DICT[str(category_id)] = []
#     with ThreadPoolExecutor(1) as executor:
#         for page in range(1, 100):
#             executor.submit(get_video_by_category, category_id,
#                             page, VIDEO_DICT[str(category_id)])
# 14693
# for data in VIDEO_DICT.values():
#     for dat in data:
#         if dat == 15126:
#             lala = data 
#             print(VIDEO_DICT.keys)
# for category_id in CATEGORY_IDS:
video_ids = []
with ThreadPoolExecutor(100) as executor:
    for i in range(1, 30001):
        # for i in VIDEO_DICT[str(category_id)]:
        executor.submit(get_content, i, video_ids)
        # get_content(i,video_ids)
        print(f'{i} - {len(video_ids)}')
totaldata = len(video_ids)
with open(f"data_tianli/{234}.txt", "w", encoding="utf-8") as f:
    for data in video_ids:
        f.write(f'{data}\n')
