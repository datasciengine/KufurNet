import json


def get_json(json_path):
    with open(json_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data


def compare_reports(json_data1, json_data2):
    # Verileri karşılaştırmak için değişkenleri tanımlıyoruz
    mismatches = []

    # json_data1 ve json_data2 içindeki anahtarların tam olarak eşit olup olmadığını kontrol ediyoruz
    if set(json_data1.keys()) != set(json_data2.keys()):
        print("Error: json_data1 and json_data2 have different keys!")
        return

    for key in json_data1:
        if json_data1[key]["Curse_Word"] and json_data2[key]["Offensive"]:
            curse_word_list1 = json_data1[key]["Curse_Word_list"]
            blacklist2 = json_data2[key]["BlackList"]
            if len(curse_word_list1) != len(blacklist2) or set(curse_word_list1) != set(blacklist2):
                mismatches.append({
                    "key": key,
                    "text": json_data1[key]["text"],
                    "curse_word_list": curse_word_list1,
                    "blacklist": blacklist2
                })

    total_count = len(json_data1)
    if total_count > 0:
        offensive_correct_percentage = (total_count - len(mismatches)) / total_count * 100
        offensive_incorrect_percentage = len(mismatches) / total_count * 100
    else:
        offensive_correct_percentage = 0
        offensive_incorrect_percentage = 0

    return {
        "Total Count": total_count,
        "Offensive Correct Percentage": round(offensive_correct_percentage, 2),
        "Offensive Incorrect Percentage": round(offensive_incorrect_percentage, 2),
        "Mismatches": mismatches
    }


def compare_reports_1(curseword_data, results_data):
    # Offensive değeri False olan ancak Curse_Word değeri True
    # Verileri karşılaştırmak için değişkenleri tanımlıyoruz
    false_positive = 0
    mismatches = []

    for key in curseword_data:
        if not results_data[key]["Offensive"] and curseword_data[key]["Curse_Word"]:
            false_positive += 1
            if curseword_data[key]["Curse_Word_list"] != results_data[key]["BlackList"]:
                mismatches.append({
                    "key": key,
                    "text": curseword_data[key]["text"],
                    "curse_word_list": curseword_data[key]["Curse_Word_list"],
                    "blacklist": results_data[key]["BlackList"]
                })

    total_count = len(curseword_data)
    if total_count > 0:
        false_positive_percentage = (false_positive / total_count) * 100
    else:
        false_positive_percentage = 0

    return {
        "Total Count": total_count,
        "False Positive Percentage": round(false_positive_percentage, 2),
        "Mismatches": mismatches
    }


curse_word_data = get_json("data/curse_word.json")
results_data = get_json("results.json")

report = compare_reports_1(curse_word_data, results_data)

with open("report.json", "w", encoding="utf-8") as file:
    json.dump(report, file, ensure_ascii=False, indent=4)
