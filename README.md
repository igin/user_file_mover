## Usage

```
python reorganize_export.py input_data1 input_data2
```


Use this script to move files from the following structure:

```
input_data1
├── userid1
│   ├── file1.txt
│   └── file2.txt
└── userid2
    ├── file1.txt
    └── file2.txt
input_data2
├── userid1
│   ├── file1.txt
│   └── file2.txt
└── userid2
    ├── file1.txt
    └── file2.txt
```

To this new structure:

```
output_data
├── userid1
│   ├── userid1_input_data1_file1.txt
│   └── userid1_input_data2_file2.txt
└── userid2
    ├── userid2_input_data1_file1.txt
    └── userid2_input_data1_file2.txt
```
