# _*_ coding: utf-8 _*_
from elasticsearch_dsl import DocType, Date, Nested, Boolean, \
    analyzer, InnerObjectWrapper, Completion, Keyword, Text, Integer

from elasticsearch_dsl.connections import connections
from elasticsearch_dsl.analysis import CustomAnalyzer as _CustomAnalyzer

connections.create_connection(hosts=["localhost"])

class CustomAnalyzer(_CustomAnalyzer):
    #防止调用这个模块的时候报错
    def get_analysis_definition(self):
        return {}

ik_analyzer = CustomAnalyzer("ik_max_word", filter=["lowercase"])

class ArticleType(DocType):
    # 设置elasticsearch的mappings
    suggest = Completion(analyzer=ik_analyzer)
    title = Text(analyzer=ik_analyzer)
    create_date = Date()
    url = Keyword()
    url_object_id = Keyword()
    front_image_url = Keyword()
    front_image_path = Keyword()
    praise_nums = Integer()
    comment_nums = Integer()
    fav_nums = Integer()
    tags = Text(analyzer=ik_analyzer)
    content = Text(analyzer=ik_analyzer)

    class Meta:
        index = 'jobbole'
        doc_type = "article"

if __name__ == "__main__":
    ArticleType.init()


class ZhiHuQuestionType(DocType):
    zhihu_id = Keyword()
    topics = Text(analyzer="ik_max_word")
    url = Keyword()
    title = Text(analyzer="ik_max_word")
    content = Text(analyzer="ik_max_word")
    answer_num = Integer()
    comments_num = Integer()
    watch_user_num = Integer()
    click_num = Integer()
    crawl_time = Date()

    class Meta:
        index = 'zhihu_question'
        doc_type = "question"

if __name__ == "__main__":
    ZhiHuQuestionType.init()