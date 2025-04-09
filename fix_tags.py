import boto3
import argparse

def update_ec2_in_region(region, dry_run=False):
    print(f"EC2 in {region}")
    session = boto3.Session(profile_name="dev")
    ec2 = session.resource('ec2', region_name='us-west-1')
    
    instances = list(ec2.instances.all())
    if not instances:
        print("No instances found.")
        return 

    if not dry_run:
        for instance in instances:
            existing_tags = [{"Key" : tag["Key"], "Value" : tag["Value"]} for tag in instance.tags or []]

            tag_present = False
            for tag in existing_tags:
                if tag["Key"] == 'Project':
                    print(f"Instance Project tag set for {instance.id} set: {tag['Value']}")
                    tag_present = True
                    break

            if not tag_present: # can factor this into a function that has a toggle based on dry run
                print("Instance Project tag missing for {instance.id}. Setting to default \'Unknown\'")
                instance.create_tags(Tags=[{"Key" : "Project", "Value" : "Unknown"}])
    else:
        for instance in ec2.instances.all():
            existing_tags = [{"Key" : tag["Key"], "Value" : tag["Value"]} for tag in instance.tags or []]
            for tag in existing_tags:
                if tag["Key"] == 'Project':
                    print(f"Instance Project tag set for {instance.id} set: {tag['Value']}")
                    tag_present = True

            if not tag_present: # can factor this into a function that has a toggle based on dry run
                print("Instance Project tag missing for {instance.id}. Setting to default \'Unknown\'")


def main(region, dry_run=False):
    print(f"Fixing Tags for {region}")
    instances = update_ec2_in_region(region, dry_run) # updates if not dry run. list all ec2 in region and identifies ec2 missing Project tag

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='FixTags')
    parser.add_argument("--region", type=str, help="Please input a region you'd like to fix tags for.")
    parser.add_argument("--dry-run", action='store_true', help="Enable dry run where changes are not made and instead displayed.")

    args = parser.parse_args()
    
    main(args.region, args.dry_run)
