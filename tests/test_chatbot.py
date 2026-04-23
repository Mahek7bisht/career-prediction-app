from models.career_predictor import predict_career

def test():
    result = predict_career("python data")
    assert result == "Data Analyst"