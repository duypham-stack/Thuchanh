import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from tkinter import *
from tkinter import filedialog

from pandas.tests.generic.test_finalize import frame_data


def open_file_dialog():
    file_path = filedialog.askopenfilename(initialdir="/", title="Chọn file", filetypes=(("CSV files", "*.csv"), ("all files", "*.*")))
    if file_path:
        display_csv_data(file_path)

def display_csv_data(file_path):
    # Clear existing widgets in the frame
    for widget in frame_data.winfo_children():
        widget.destroy()

    # Read CSV data using pandas
    df = pd.read_csv(file_path)
    global in_data
    in_data = pd.read_csv(file_path, index_col = 0).values

    # Display header
    for col, header_value in enumerate(df.columns):
        label = Label(frame_data, text=header_value, padx=10, pady=5)
        label.grid(row=0, column=col)

    # Display data
    for row, (_, data) in enumerate(df.iterrows(), start=1):
        for col, value in enumerate(data):
            label = Label(frame_data, text=value, padx=10, pady=5)
            label.grid(row=row, column=col)

def create_repost(label_result=None):
    sv = in_data[:,1]
    tongsv = sv.sum()

    svF = in_data[:,10]
    svDat = np.subtract(sv,svF)
    svTruot = np.subtract(sv,svDat)
    sumDat = svDat.sum()
    sumTruot = svTruot.sum()
    tyle_dat = np.divide(np.sum(svDat),np.sum(sv))*100
    tyle_truot = 100 - tyle_dat

    svA_B = in_data[:,2:5+1]
    sumA_B = np.sum(svA_B)
    svC_D = in_data[:,6:9+1]
    sumC_D = np.sum(svC_D)
    sumF = np.sum(svF)

    svA = in_data[:,3]
    maxA = svA.max()
    i1 = np.where(svA == maxA)
    maxF = svF.max()
    minF = svF.min()
    i2 = np.where(svF == minF)
    i3 = np.where(svF == maxF)

    svBp = in_data[:,4]
    svB = in_data[:,5]
    svCp = in_data[:,6]
    svC = in_data[:,7]
    svDp = in_data[:,8]
    svD = in_data[:,9]

    label_result.config(text="-Tổng sinh viên dự thi: "+f"{tongsv} sinh viên\n"
                        + "-Số sinh viên đạt: "+f"{sumDat} sinh viên\n"
                        + "-Số sinh viên trượt: "+f"{sumTruot} sinh viên\n"
                        + "-Tỷ lệ sinh viên đạt: "+f"{tyle_dat} %\n"
                        + "-Tỷ lệ sinh viên trượt: "+f"{tyle_truot} %\n"
                        + "-Số sinh viên có điểm khá/giỏi là: "+f"{sumA_B} sinh viên\n"
                        + "-Số sinh viên có điểm TB/yếu là: "+f"{sumC_D} sinh viên\n"
                        + "-Số sinh viên có điểm kém (trượt) là: "+f"{sumF} sinh viên\n"
                        + "-Lớp có nhiều điểm A nhất là: {0} có {1} sinh viên đạt điểm A\n".format(in_data[i1,0],maxA)
                        + "-Lớp có ít điểm F nhất là: {0} có {1} sinh viên đạt điểm F\n".format(in_data[i2,0],minF)
                        + "-Lớp có nhiều điểm F nhất là: {0} có {1} sinh viên đạt điểm F\n".format(in_data[i3,0],maxF))