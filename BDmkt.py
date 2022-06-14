import requests, json, openpyxl
def main(date, cookie, data, location1, location2, location3):
    try:
        url = 'https://fengchao.baidu.com/hairuo/request.ajax'
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        }
        data['params'] = data['params'].replace("yyyy-mm-dd", date) # 替换日期

				# 发送模拟网络请求，并解析返回的json数据：
        response = requests.post(url, headers=headers, cookies=cookie, data=data)
        result = response.text
        result = json.loads(result)

				# 解析展现、点击、消费的推广数据：
        impression = result['data']['summary']['impression']
        click = result['data']['summary']['click']
        cost = result['data']['summary']['cost']

    except:
        impression = 'error'
        click = 'error'
        cost = 'error'

		print(impression, click, cost)  # 打印展现、点击、消费的推广数据
    
		# 导入模板：
    templ = r'推广数据.xlsx'
    wb = openpyxl.load_workbook(templ)
    ws = wb['Sheet1']

    # 写入数据：
    ws[location1].value = impression
    ws[location2].value = click
    ws[location3].value = cost

    # 保存文件  过程中需关闭文件，执行完成后打开即可
    wb.save(r'推广数据.xlsx')

# main()  # 运行测试
