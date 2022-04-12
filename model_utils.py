# import tensorflow as tf
# from transformers import BertModel, BertTokenizer
#
# # 加载本地预训练模型
# def load_model(model_name):
#     model = BertModel.from_pretrained(model_name)
#     return model
#
# # 数据生成器
# def data_generator(data, tokenizer, max_len):
#     for text in data:
#         text = tokenizer.tokenize(text)
#         text = text[:max_len-2]
#         text = tokenizer.convert_tokens_to_ids(text)
#         text = [101] + text + [102]
#         yield text
#
# # 加载预训练模型分词器
# def load_tokenizer(model_name):
#     tokenizer = BertTokenizer.from_pretrained(model_name)
#     return tokenizer
#
# # 预测token embedding
# def predict_token_embedding(model, tokenizer, text):
#     # 加载预训练模型
#     model = load_model(model_name)
#     # 加载预训练模型分词器
#     tokenizer = load_tokenizer(model_name)
#     # 数据生成器
#     data_generator = data_generator(text, tokenizer, max_len=512)
#     # 预测
#     outputs = model(next(data_generator))
#     # 输出
#     return outputs[0][0][0]
#
# # bert文本分类
# def bert_text_classification(model_name, text):
#     # 加载预训练模型
#     model = load_model(model_name)
#     # 加载预训练模型分词器
#     tokenizer = load_tokenizer(model_name)
#     # 数据生成器
#     data_generator = data_generator(text, tokenizer, max_len=512)
#     # 预测
#     outputs = model(next(data_generator))
#     # 输出
#     return outputs[0][0][0]
#
# # 训练bert文本多分类模型
# def bert_text_multi_classification(model_name, train_data, train_label, test_data, test_label):
#     # 加载预训练模型
#     model = load_model(model_name)
#     # 加载预训练模型分词器
#     tokenizer = load_tokenizer(model_name)
#     # 数据生成器
#     train_data_generator = data_generator(train_data, tokenizer, max_len=512)
#     test_data_generator = data_generator(test_data, tokenizer, max_len=512)
#     # 模型训练
#     model.fit(train_data_generator, train_label, epochs=3)
#     # 模型预测
#     outputs = model.predict(test_data_generator)
#     # 输出
#     return outputs
#
#
