import json

__search_config__ = """
{"search_home":"/Users/gaoyan/project/IVY/data"}
"""
def get_search_home():
    return json.loads(__search_config__)

