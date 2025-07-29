import datetime

def parse_ssh_log(filename,filter_by=None):
    with open(filename, 'r') as file:
        lines = file.readlines()
    print(f"\nFilter: {filter_by if filter_by else 'ALL'}\n")
    print(f"{'Time':<20} {'Src IP':<18} {'Src Port':<10} {'Dst IP':<18} {'Dst Port':<10} {'Result':<12} {'Direction':<10} {'Client Version':<25} {'Server Version'}")
    print("=" * 130)

    for line in lines:
        fields = line.strip().split('\t')
        if len(fields) < 11:
            continue  # Skip malformed lines

        # Convert timestamp string to float, then to datetime
        try:
            timestamp = datetime.datetime.fromtimestamp(float(fields[0])).strftime('%d-%m-%Y %H:%M:%S')
        except Exception as e:
            print("Invalid time", e)


        #timestamp = fields[0]
        src_ip = fields[2]
        src_port = fields[3]
        dst_ip = fields[4]
        dst_port = fields[5]
        result = fields[6]
        direction = fields[7]
        client_version = fields[8]
        server_version = fields[9]

        if filter_by and result !=filter_by.lower():
            continue


        print(f"{timestamp:<20} {src_ip:<18} {src_port:<10} {dst_ip:<18} {dst_port:<10} {result:<12} {direction:<10} {client_version:<25} {server_version}")

if __name__ == "__main__":
    log_file = "ssh_log.txt.log"  # Replace with your actual file name
   
    print("choose your option:")
    print("1.shows only SUCCESS logs")
    print("2.shows only FAILURE logs")
    print("3.shows only UNDETERMINED logs")
    print("4.shows ALL logs")
    choice=input("enter your choice(1-4):")

    filter_option=None
    if choice=="1":
        filter_option="SUCCESS"
    elif choice=="2":
        filter_option="FAILURE"
    elif choice=="3":
        filter_option="UNDETERMINED"        
    elif choice=="4":
        filter_option=None
    else:
        print("Invalid choice.Showing all logs")
        

    parse_ssh_log(log_file,filter_by=filter_option)
