- bỏ các cột trùng lặp
- thay thế (thay bằng giá trị trung bình -> đưa move to right vào + thay bằng giá trị trung bình)
- xử lí z-score + vẽ biểu đồ
- PT thăm dò

self.data["TotalPrice"] = self.data.apply(
lambda row: row["UnitPrice"] \* row["Quantity"], axis=1
)
no_outliers_df = self.data[(np.abs(stats.zscore(self.data["TotalPrice"])) < 3)]
fig, ax = plt.subplots()
ax.boxplot(no_outliers_df["TotalPrice"])
plt.show()

# Xác định tập DL Input (X) và DL đầu ra (y)
            self.data = self.data.copy()
            X = self.data.loc[:, self.data.columns != "Quatity"]
            y = self.data["Quantity"]

            label_encoder = LabelEncoder()
            y = label_encoder.fit_transform(y)

            # Áp dụng SelectKBest với k=3
            selector = SelectKBest(chi2, k="all")
            selector.fit(X, y)

            # Lấy danh sách các đặc trưng quan trọng đã chọn
            selected_columns = X.columns[selector.get_support(indices=True)]
            result_text = "Các đặc trưng quan trọng:\n"
            for col in selected_columns:
                result_text += "- {}\n".format(col)

            # Chèn kết quả vào widget Text
            self.text.insert("end", result_text)

            self.data = self.data[selected_columns]
            parent.data = self.data
