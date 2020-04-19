# 爬虫


from pyquery import PyQuery as pq
import requests
import json

# type: movie
# tag: 豆瓣高分
# sort: recommend
# page_limit: 20
# page_start: ?
page_url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&sort' \
           '=recommend&page_limit=20&page_start='
movie_detail_url = 'https://movie.douban.com/j/subject_abstract?subject_id='
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/80.0.3987.163 Safari/537.36 '
}


def get_one_page(page_start, results):
    url = page_url + str(page_start)

    html = requests.get(url, headers=headers).text
    subjects = json.loads(html)['subjects']
    for movie in subjects:
        movie_id = movie['id']  # 电影id
        title = movie['title']  # 电影标题
        rate = movie['rate']  # 电影评分
        movie_url = movie['url']  # 电影链接
        cover_url = movie['cover']  # 电影图片
        cover_x = movie['cover_x']  # 电影图片长
        cover_y = movie['cover_y']  # 电影图片宽
        movie_info_detail_url = movie_detail_url + str(movie_id)  # 获取电影详细信息链接
        movie_html = requests.get(movie_info_detail_url, headers=headers).text  # 获取电影详细信息
        movie_detail_subject = json.loads(movie_html)['subject']  # 电影详细信息
        directors = movie_detail_subject['directors']  # 导演s
        actors = movie_detail_subject['actors']  # 演员s
        duration = movie_detail_subject['duration']  # 时长
        region = movie_detail_subject['region']  # 地区
        types = movie_detail_subject['types']  # 类型
        release_year = movie_detail_subject['release_year']  # 上映时间
        result_map = {'movie_id': movie_id, 'title': title, 'rate': rate, 'movie_url': movie_url,
                      'cover_url': cover_url, 'cover_x': cover_x, 'cover_y': cover_y, 'directors': directors,
                      'actors': actors, 'duration': duration, 'region': region, 'types': types,
                      'release_year': release_year}
        results.append(result_map)


def get_top100():
    results = []
    for i in range(0, 100, 20):
        get_one_page(i, results)
    return results


def main():
    results = []
    for i in range(0, 100, 20):
        get_one_page(i, results)


# main()
