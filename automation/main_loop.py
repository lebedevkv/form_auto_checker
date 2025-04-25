import pandas as pd
from automation.checker import EmployeeChecker

OUTPUT_PATH = "output_result.xlsx"

def run_all_checks(driver, log_fn, input_path):
    df = pd.read_excel(input_path, skiprows=4)  # F5 = index 0
    log_fn(f"📂 Загружено сотрудников: {len(df)}")

    comments = []
    for index, row in df.iterrows():
        log_fn(f"\n🧾 Проверка сотрудника №{index + 1}...")
        employee_data = {
            "Дата рождения": str(row["F"]),
            "Серия": str(row["K"]),
            "Номер": str(row["L"]),
            "Дата выдачи": str(row["M"])
        }
        checker = EmployeeChecker(driver, log_fn, employee_data)
        comment = checker.run_check()
        comments.append(comment)

    df["Комментарий"] = comments
    df.to_excel(OUTPUT_PATH, index=False)
    log_fn(f"\n💾 Результат сохранён в: {OUTPUT_PATH}")