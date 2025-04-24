# automation/main_loop.py
import pandas as pd
from automation.checker import EmployeeChecker

INPUT_PATH = "input.xlsx"
OUTPUT_PATH = "output_result.xlsx"

def run_all_checks(driver, log_fn, input_path=INPUT_PATH, output_path=OUTPUT_PATH):
    # Загружаем Excel
    df = pd.read_excel(input_path, skiprows=4)  # F5 = index 0
    log_fn(f"📂 Загружено сотрудников: {len(df)}")

    # Обрабатываем всех
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

    # Добавляем колонку комментариев
    df["Комментарий"] = comments
    df.to_excel(output_path, index=False)
    log_fn(f"\n💾 Результат сохранён в: {output_path}")