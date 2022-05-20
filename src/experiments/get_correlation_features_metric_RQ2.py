




if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(description='Managerie plot on csv file')
        parser.add_argument('--jsonsf', metavar='path', required=True,
                            help='path to images')
        parser.add_argument('--results', metavar='path', required=True,
                            help='path to images')
        parser.add_argument('--csv', metavar='path', required=True,
                            help='path to images')
        args = parser.parse_args()
        if args.jsonsf == "" or args.results == "" or args.csv == "":
            print("Please, check your input parameters")
    except Exception as e:
        print(e)
        sys.exit(1)
    dm, negatives, positives = data_means(json_file=args.jsonsf, results_file=args.results, couples_csv_file=args.csv)
    title = args.csv.split(".")[-2].split("/")[-1]
    title = "managerie_"+title
    plot(dm, negatives, positives, title)