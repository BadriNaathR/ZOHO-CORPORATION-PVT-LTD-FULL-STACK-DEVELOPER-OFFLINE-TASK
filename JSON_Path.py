import json
import random
def generate_sample(json_structure, num_samples):
    samples = []
    for _ in range(num_samples):
        sample = {}
        for field in json_structure:
            k = field['key'] #key = k
            data_type = field['type']
            if data_type == 'string':
                sample[k] = 'sample'
            elif data_type == 'number':
                sample[k] = random.randint(20, 30)#give range
            elif data_type == 'boolean':
                sample[k] = random.choice([True, False])
        samples.append(sample)
    return samples
json_struc = json.loads(input("Enter the JSON Structure: "))
n = int(input("Enter no of sample to generate "))
sample_jsons = generate_sample(json_struc, n)
print(json.dumps(sample_jsons, indent=2))