# beancount_bot_costflow

[beancount_bot](https://github.com/kaaass/beancount_bot) 的 Costflow 语法插件

![GitHub](https://img.shields.io/github/license/kaaass/beancount_bot_costflow)
![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/kaaass/beancount_bot_costflow?color=green&label=version)
![PyPI](https://img.shields.io/pypi/v/beancount_bot_costflow)

## 使用

使用本插件之前，需要保证安装 Node.js 并且安装路径位于 PATH 中。

1. 安装：`pip install beancount_bot_costflow`
2. 在 beancount_bot 配置文件的 `transaction.message_dispatcher` 增加如下配置：

```yaml
transaction:
  # ...
  message_dispatcher:
    # ...
    # 必须添加在最后一个位置
    - class: 'beancount_bot_costflow.CostflowDispatcher'
      args:
        costflow_config: 'costflow.json'
```

注意，你仍需要自行配置一份 `costflow.json` 作为 Costflow 语法的配置。参阅：

- Costflow 文档：https://www.costflow.io/docs/syntax/
- Costflow Playground：https://playground.costflow.io

## Note

Costflow 部分（`costflow-parser.js`）源码位于：[kaaass/costflow-parser-simple-wrapper](https://github.com/kaaass/costflow-parser-simple-wrapper)

与本仓库同采用 GPLv3 协议。

## Credit

[costflow/parser](https://github.com/costflow/parser)
