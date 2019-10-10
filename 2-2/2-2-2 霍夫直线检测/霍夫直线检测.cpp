/*
******************************************************************************
* @file       霍夫直线检测.cpp
* @author     Xiaoxiao
* @date       2019-10-10
* @version    3.4.3
* @brief      用霍夫直线来检测图片1的灯条
* @attention  HoughLinesP函数
******************************************************************************
*/
#include <opencv2/opencv.hpp>
#include <iostream>
#include <math.h>
#include <vector>


int main(int argc, char** argv) {
	cv::Mat src, gray, dst;
	src = cv::imread("H:\\RM二面\\图片1.jpg");
	if (!src.data) {
		printf("could not load image...\n");
		return -1;
	}
	cv::imshow("src", src);
	
	// 进行霍夫线条检测前先检测边缘
	cv::Canny(src, gray, 100, 200);
	cvtColor(gray, dst, CV_GRAY2BGR);
	imshow("edge", dst);


	std::vector<cv::Vec4f> plines;        
	HoughLinesP(gray, plines, 1, CV_PI / 180.0, 10, 0, 10);
	// 2 输出的极坐标，表示直线 3 像素扫描步长 4 角度扫描步长
	// 5 阈值 6 最小直线长度 7 最大间隔

	for (size_t i = 0; i < plines.size(); i++)
	{
		cv::Vec4f hline = plines[i];
		line(dst, cv::Point(hline[0], hline[1]), cv::Point(hline[2], hline[3]), \
			cv::Scalar(0, 0, 255), 3, cv::LINE_AA);
	}

	cv::imshow("hough-line-detection", dst);
	cv::waitKey(0);
	return 0;
}