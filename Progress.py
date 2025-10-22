import os, json
import numpy as np
import torch
import sys, time, math

class StaticProgress:
    def __init__(self, total, desc="Progress", step_percent=0.05, unit="it", rank=0, disable=False):
        """
        非交互式进度显示器
        Args:
            total (int): 总步数
            desc (str): 前缀描述
            step_percent (float): 每多少百分比打印一次
            unit (str): 单位（如 it/batch/sample）
            rank (int): 多GPU时只打印rank=0
            disable (bool): 关闭输出
        """
        self.total = total
        self.desc = desc
        self.step = max(1, int(total * step_percent))
        self.rank = rank
        self.disable = disable or (rank != 0)
        self.unit = unit
        self.start_time = None
        self.last_time = None
        self.counter = 0

    def start(self):
        """开始计时"""
        self.start_time = self.last_time = time.time()
        if not self.disable:
            print(f"[{self.desc}] Start | total={self.total} {self.unit}")

    def update(self, n=1, **metrics):
        """
        更新进度
        Args:
            n: 当前步数增量
            metrics: 附加信息，如 loss=0.123, delta=0.0001
        """
        if self.disable: return

        self.counter += n
        if self.counter % self.step != 0 and self.counter < self.total:
            return

        now = time.time()
        elapsed = now - self.start_time
        rate = self.counter / elapsed if elapsed > 0 else 0
        remaining = (self.total - self.counter) / rate if rate > 0 else math.inf

        # 构建日志字符串
        pct = self.counter / self.total * 100
        metric_str = " ".join([f"{k}={v:.4f}" if isinstance(v, (int, float)) else f"{k}={v}"
                               for k, v in metrics.items()])
        log = (f"[{self.desc}] {pct:5.1f}% | "
               f"{self.counter:>6}/{self.total:<6} | "
               f"{rate:7.2f} {self.unit}/s | "
               f"ETA {remaining:6.1f}s"
               + (f" | {metric_str}" if metric_str else ""))
        print(log, flush=True)

    def done(self, **metrics):
        """结束显示"""
        if self.disable: return
        total_time = time.time() - self.start_time
        metric_str = " ".join([f"{k}={v:.4f}" if isinstance(v, (int, float)) else f"{k}={v}"
                               for k, v in metrics.items()])
        print(f"[{self.desc}] Done | total_time={total_time:.2f}s | {metric_str}", flush=True)

