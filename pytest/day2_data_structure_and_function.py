


def build_url(base_url="http://example.com", path='', **params):
    """
    构建一个格式正确、经过编码的完整URL字符串。
    这是接口自动化测试中构建请求地址的核心工具函数。

    设计原则（健壮性体现）：
    1. 输入验证：确保关键参数类型正确。
    2. 防御拼接：自动修正路径斜杠，避免双斜杠或缺失斜杠。
    3. 条件执行：仅在有必要时添加查询字符串。
    4. 安全编码：对参数值进行URL编码，保证特殊字符的传输安全。

    Args:
        base_url (str): 基础URL地址，默认'http://example.com'。
        path (str): 请求路径，例如 '/api/v1/user'。
        **params: 任意数量的关键字参数，将作为查询参数拼接。

    Returns:
        str: 拼接并编码后的完整URL。

    Raises:
        TypeError: 当base_url或path不是字符串类型时。
    """


    if not isinstance(base_url, str):
        raise TypeError(f"参数 'base_url' 必须是字符串，而不是 {type(base_url).__name__}")
    if not isinstance(path, str):
        raise TypeError(f"<UNK> 'path' <UNK> {type(path).__name__}")
    if not base_url.endswith("/"):
        base_url = base_url + "/"
    full_url = base_url + path.lstrip("/")
    if params:
        from urllib.parse import quote

        full_url += '?' + "&".join([f"{k}=quote(str({v}))" for k, v in params.items()])
    return full_url

if __name__ == '__main__':
    print("=== 正常用例测试 ===")
    print(build_url('/api/user', id=1, name='alice'))
    print(build_url('https://real.api.com', '/v2/login', username='张 三', token='abc&def'))

    try:
        print(build_url(None, id=1, name='alice'))
    except TypeError as e:
        print(e)
