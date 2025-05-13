
        try:
            # Generate output
            generate_ids = model.generate(**inputs, max_length=200)
            generated_text = processor.batch_decode(generate_ids, skip_special_tokens=True)

            # Write output to file
            for index in range(len(generated_text)):
                text = generated_text[index].split("ASSISTANT:")[-1]
                with open(paths[index][0], 'w') as f:
                    f.write(text.replace('\n', ' '))

        except Exception as e:
            # Handle errors gracefully and log them
            with open(os.path.dirname(paths[0][0]) + "_abnormal.txt", 'a') as f:
                f.write(os.path.basename(paths[0][0]) + "\n")

            # Write empty output if error occurs