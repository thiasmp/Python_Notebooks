import argparse
import webget

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A program that downloads a URL and stores it locally')
    parser.add_argument('url', help='The URL to process')
    parser.add_argument('-d','--destination', default='default-file.dat')

    args = parser.parse_args()
    print(args.url, args.destination)
    webget.download(args.url, args.destination)