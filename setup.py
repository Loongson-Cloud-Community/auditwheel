from __future__ import annotations

from setuptools import setup

extras = {
    "test": ["pytest>=3.4", "jsonschema", "pypatchelf", "pretend", "docker"],
    "coverage": ["pytest-cov"],
}
extras["develop"] = sum(extras.values(), [])
extras["coverage"] += extras["test"]

# 添加版本号字段
setup(
    name="auditwheel",  # 项目名称
    version="6.1.0",  # 在这里设置版本号
    extras_require=extras
)

#setup(extras_require=extras)
