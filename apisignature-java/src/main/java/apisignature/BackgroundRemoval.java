package apisignature;

import org.opencv.imgproc.Imgproc;

import java.util.ArrayList;
import java.util.Arrays;

import org.opencv.core.Core;
import org.opencv.core.Mat;
import org.opencv.core.Size;
import org.opencv.imgcodecs.Imgcodecs;

public class BackgroundRemoval {
	public static void main(String[] args) {
		nu.pattern.OpenCV.loadLocally();
		
		Mat image = new Mat();
		Mat alpha = new Mat();
		
		image = Imgcodecs.imread("/home/welmends/signature.jpg", Imgcodecs.IMREAD_COLOR);
		
		Imgproc.GaussianBlur(image, image, new Size(3,3), 1);
		Imgproc.cvtColor(image, image, Imgproc.COLOR_BGR2GRAY);
		Imgproc.threshold(image, image, 0, 255, Imgproc.THRESH_BINARY+Imgproc.THRESH_OTSU);
		Imgproc.threshold(image, alpha, 0, 255, Imgproc.THRESH_BINARY_INV+Imgproc.THRESH_OTSU);
		Core.merge(new ArrayList<>(Arrays.asList(image, image, image, alpha)), image);
		
		Imgcodecs.imwrite("/home/welmends/signature2.png", image);
	}
}
