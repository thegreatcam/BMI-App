import pytest
from QA2 import convertW, convertH, calcBMI, getClass 

#test the convertW function
@pytest.mark.parametrize("weight, output",[(150, 68.1),(160,72.64),(170,77.18),(180,81.72)])
def test_convertW(weight, output):
    assert convertW(weight)==pytest.approx(output,0.01)

#tests the convertH function
@pytest.mark.parametrize("height, output",[(70, 3.161284),(60, 2.322576),(65, 2.725801),(75, 3.629025)])
def test_convertH(height, output):
    assert convertH(height)==pytest.approx(output,0.01)

#tests the calcBMI function
@pytest.mark.parametrize("w, h, bmi",[(68.1, 3.161284, 21.54),(72.64, 2.322576, 31.28),(77.18, 2.725801, 28.31),(81.72, 3.629025, 22.51)])
def test_calcBMI(w, h, bmi):
    assert calcBMI(w,h)==pytest.approx(bmi,0.01)

#tests the getClass function using the weak Nx1 boundary testing technique
@pytest.mark.parametrize("bmi, output",[(18.5, "Normal weight"),(18.4, "Normal weight"),(24.9, "Normal weight"),(25, "Overweight"), 
(25.1,"Overweight"),(29.9, "Overweight"),(30, "Obese")])
def test_getClass(bmi, output):
    assert getClass(bmi)==output
    

