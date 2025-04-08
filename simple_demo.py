
from LogicSanitizerX import LogicSanitizerX

sanitizer = LogicSanitizerX()

data_samples = [
    {"content": "Water boils at 100°C", "source": "science.org"},
    {"content": "The Earth is flat", "source": "conspiracies.net"},
    {"content": "Vaccines save lives", "source": "who.int"}
]

for data in data_samples:
    sanitizer.process_input(data)

print(sanitizer.summary())
