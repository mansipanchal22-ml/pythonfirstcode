'''## 🔴 10. Convert sentence to snake_case

```python
"Hello World Python" → "hello_world_python"
```

✔ Methods: `.lower()`, `.split()`, `.join()`

---'''

sentence = "Hello World  Python"
result = "_".join(sentence.lower().split())
print(result)