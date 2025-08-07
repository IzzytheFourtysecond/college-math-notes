import numpy as np

def angleTest(theta_vec):
	# Step 1: Make a matrix whose columns are each of the unit vectors with angle θ_i off the horizontal.
	vecMatrix = np.array([
		[np.cos(theta_vec[0] * 2 * np.pi), np.cos(theta_vec[1] * 2 * np.pi), np.cos(theta_vec[2] * 2 * np.pi)],[np.sin(theta_vec[0] * 2 * np.pi), np.sin(theta_vec[1] * 2 * np.pi), np.sin(theta_vec[2] * 2 * np.pi)]])

	# Step 2: Generate a vector: epsVec, in {-1, 1}^3. Then measure the length of vecMatrix @ epsVec. Our goal is to find the minimum length
	minLength = 4
	for i in (-1, 1):
		for j in (-1, 1):
			for k in (-1, 1):
				epsVec = np.array([[i],[j],[k]])

				minLength = min(minLength, np.linalg.norm(vecMatrix @ epsVec))

	return minLength


def anglePicker(testFreq):
	maxLength = 0
	for i in range(0, testFreq - 2):
		MaxLengthFixingI = 0
		for j in range(i, testFreq - 1):
			MaxLengthFixingJ = np.max(np.array([angleTest([i / testFreq, j / testFreq, k / testFreq]) for k in range(j, testFreq)]))

			MaxLengthFixingI = max(0, MaxLengthFixingJ)
		
		MaxLength = max(0, MaxLengthFixingI)
	
	return MaxLength



print(anglePicker(90))

