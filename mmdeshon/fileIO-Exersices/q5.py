with open('q5_file1') as f51:
    with open('q5_file2') as f52:
        with open('q5_result', 'w') as final_file:
            time_count = len(f51.readlines())
            f51.seek(0)
            for time in range(time_count):
                final_file.write(f'{f51.readline().strip()} {f52.readline()}')
