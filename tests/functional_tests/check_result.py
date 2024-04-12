import os, json, sys

def compare_result_log(test_reaults_path:str):

    details_path = test_reaults_path + "/logs/details/"
    host_path    = os.listdir(details_path)[0]
    id_path      = os.listdir(details_path + "/" + host_path)[0]
    attempt_path = os.listdir(details_path + "/" + host_path + "/" + id_path)[0]
    results_path = (os.listdir(details_path + "/" + host_path + "/" + id_path+ "/" + attempt_path))
    results_path.sort()
    result_path  = details_path + "/" + host_path + "/" + id_path + "/" + attempt_path + "/" + results_path[-1] + "/stdout.log"

    with open(result_path, 'r') as file:
        lines = file.readlines()

    result_json = {}
    result_json["lm loss:"] = {"values":[]}

    for line in lines:
        if line[0:10] == " iteration":
            line_split = line.strip().split("|")
            for key_value in line_split:
                if key_value[0:9] == " lm loss:":
                    result_json["lm loss:"]["values"].append(float(key_value.split(':')[1]))

    gold_log_path = test_reaults_path + "/../gold_result/gold_result.json"

    with open(gold_log_path, 'r') as f:
        gold_result_json = json.load(f)
    
    print("\nresult checking")
    print("result: ", result_json)
    print("gold_result: ", gold_result_json)
    print("The results are consistent: ", result_json == gold_result_json)

if __name__ == '__main__':
    test_reaults_path = sys.argv[1]
    compare_result_log(test_reaults_path)
    