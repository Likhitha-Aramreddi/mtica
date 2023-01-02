sample_dict={
    'Physics': 82,
    'Math': 65,
    'History': 75
    }
print(min(sample_dict , key=sample_dict.get))
print(max(sample_dict , key=sample_dict.get))
print(round(sample_dict , key=sample_dict.get))

