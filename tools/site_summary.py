import json
from datetime import datetime
from collections import OrderedDict


# 内置站点资料集合
SITES = [
    {
        "name": "华体会首页",
        "url": "https://homeweb-hth.com.cn",
        "keywords": ["华体会", "体育", "娱乐", "首页"],
        "tags": ["体育", "综合", "品牌官网"],
        "description": "华体会官方首页，提供体育赛事、娱乐互动等综合服务。"
    },
    {
        "name": "华体会新闻中心",
        "url": "https://homeweb-hth.com.cn/news",
        "keywords": ["华体会", "新闻", "资讯", "动态"],
        "tags": ["新闻", "资讯", "更新"],
        "description": "华体会最新动态、行业资讯与活动公告的汇聚平台。"
    },
    {
        "name": "华体会产品服务",
        "url": "https://homeweb-hth.com.cn/services",
        "keywords": ["华体会", "产品", "服务", "解决方案"],
        "tags": ["服务", "产品", "帮助"],
        "description": "详细介绍华体会提供的各类服务与产品解决方案。"
    },
    {
        "name": "华体会关于我们",
        "url": "https://homeweb-hth.com.cn/about",
        "keywords": ["华体会", "公司", "简介", "团队"],
        "tags": ["关于", "简介", "团队"],
        "description": "了解华体会公司背景、发展历程与核心团队信息。"
    }
]


def load_site_data():
    """
    返回内置站点数据，允许外部扩展或未来替换。
    """
    return SITES


def generate_summary_for_site(site):
    """
    为单个站点生成结构化摘要字典。
    """
    summary = OrderedDict()
    summary["名称"] = site["name"]
    summary["URL"] = site["url"]
    summary["核心关键词"] = ", ".join(site["keywords"])
    summary["标签"] = ", ".join(site["tags"])
    summary["简介"] = site["description"]
    summary["记录时间"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return summary


def build_full_summary(sites):
    """
    构建所有站点的完整结构化摘要。
    """
    full = OrderedDict()
    full["生成时间"] = datetime.now().isoformat()
    full["站点总数"] = len(sites)
    full["站点列表"] = [generate_summary_for_site(s) for s in sites]
    return full


def export_summary_to_json(summary, filepath=None):
    """
    将摘要输出为 JSON 字符串，可选写入文件。
    """
    json_str = json.dumps(summary, ensure_ascii=False, indent=2)
    if filepath:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(json_str)
    return json_str


def print_summary_pretty(summary):
    """
    以可读格式打印摘要信息。
    """
    print("=" * 60)
    print("站点摘要报告")
    print("生成时间:", summary.get("生成时间"))
    print("站点总数:", summary.get("站点总数"))
    print("-" * 60)
    for idx, site in enumerate(summary.get("站点列表", []), 1):
        print(f"\n--- 站点 {idx} ---")
        for key, value in site.items():
            print(f"{key}: {value}")
    print("=" * 60)


def main():
    """
    主入口：加载数据、生成摘要、输出结果。
    """
    site_data = load_site_data()
    full_summary = build_full_summary(site_data)

    # 打印美观版
    print_summary_pretty(full_summary)

    # 导出为 JSON 字符串
    json_output = export_summary_to_json(full_summary)
    print("\n\nJSON 格式输出:\n")
    print(json_output)

    # 可选保存到文件
    # export_summary_to_json(full_summary, "site_summary.json")


if __name__ == "__main__":
    main()