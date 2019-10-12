def parse_tf_output(output):
    output = output.decode()
    output_list = output.split('-')[2:]
    output_metrics = {value.split(':')[0].strip(): value.split(':')[1].strip()
                      for value in output.split('-')[2:]}
    return output_metrics

