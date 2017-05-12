# !/usr/bin/python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Name:        watchflatness.py
# Purpose:     In README.md
#
# Author:      Kilo11
#
# Created:     10/05/2017
# Copyright:   (c) SkyDog 2017
# Licence:     SDS100**
# -----------------------------------------------------------------------------
""" 樹脂材料の平滑確認 """

# モジュール インポート
import cv2
import numpy as np

ok_cap = cv2.imread("ng_vibrator_sampl.png")
ng_cap = cv2.imread("ok_vibrator_sampl.png")
# cap = cv2.imread("test.png")

while(True):
    # ret, frame = cap.read()
    ok_frame = ok_cap
    ng_frame = ng_cap
    # HSV変換
        # HSV
            # Hue/Saturation/Brightness
    ok_hsv = cv2.cvtColor(ok_frame, cv2.COLOR_BGR2HSV)
    ng_hsv = cv2.cvtColor(ng_frame, cv2.COLOR_BGR2HSV)

    # 取得色範囲 指定
    # lower_color = np.array([20, 50, 50])
    # upper_color = np.array([100, 255, 255])
    # lower_color = np.array([0, 0, 0])
    # upper_color = np.array([255, 255, 60])

    # lower_color = np.array([0, 0, 200])
    # upper_color = np.array([120, 255, 255])

    lower_color = np.array([50, 50, 50])
    upper_color = np.array([70, 255, 255])

    # 指定色のマスク画像 生成
    ok_mask = cv2.inRange(ok_hsv, lower_color, upper_color)
    ng_mask = cv2.inRange(ng_hsv, lower_color, upper_color)

    # フレームとマスク画像の共通の領域 抽出
    ok_color = cv2.bitwise_and(ok_frame, ok_frame, mask=ok_mask)
    ng_color = cv2.bitwise_and(ng_frame, ng_frame, mask=ng_mask)

    cv2.imshow("OK", ok_color)
    cv2.imshow("NG", ng_color)
    # cv2.imshow("SHOW COLOR IMAGE", frame)

    # "q" 押下 終了
    k = cv2.waitKey(1)
    if k == ord("q"):
        cv2.destroyAllWindows()
        break

# cap.release()
