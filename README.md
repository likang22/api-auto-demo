## 🚚 接口自动化链路 Demo（可在线跑）
- 场景：下单-支付-查询-删除（基于 httpbin 模拟）
- 技术：Python3 + Requests + Pytest + Allure
- CI：GitHub Actions（下一步接入）
- 一键运行：
  ```bash
  git clone https://github.com/你的用户名/api-auto-demo.git
  cd api-auto-demo
  pip install -r requirements.txt
  pytest cases/test_httpbin_flow.py --alluredir=report
  allure open report
