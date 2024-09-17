# 🚀 Terraform Questions 

## Level: Easy

1. A Junior DevOps engineer has just joined your organization. He is exploring ways to automate the existing process of infrastructure provisioning and management using code. As his tech lead, what suggestions in general would you like to provide him?
2. Your company has recently been contracted to oversee a business transformation project for a large bank. This project requires a lot of the legacy banking applications to be migrated to several different cloud platforms - AWS, Azure, GCP to name a few. The solution architects of your team have decided to go with Terraform as their choice for the infrastructure provisioning. Why do you think they went with this choice?
3. Choose the correct terraform command to display the blueprint of the infrastructure to be applied.
4. Which of the following is an "argument" used in the sample terraform configuration given below?
```tf
resource "aws_instance" "webserver" { 
  ami           = "ami-0edab43b6fa892279"
  instance_type = "t2.micro"
}
```
5. What is the order of commands to be run in a core terraform workflow?
6. Which of the options can be used to run a terraform apply without confirmation?
7. A simple terraform configuration file is given below. What is the name of the resource that will be created?
```tf
resource "local_file" "pet" {​
  filename = "/root/pets.txt"​
  content = "We love pets!"​ ​
}
```
8. Select the file extension used by terraform configuration files.
9. What is the resource type used by this sample configuration file?
```tf
resource "google_compute_instance" "my-testvm" {
  count        = 3
  name         = my-testvm${count.index + 1}"
  machine_type = var.instance_type
  zone         = var.zone
  tags = ["testvm"]
  }
```
10. What is Immutable Infrastructure?
11. After testing a sample terraform code, the user now wants to get rid of everything that was provisioned. Which of the following does he need to execute in order to accomplish this?
12. What should be the very first command that should be run after writing a new Terraform configuration or cloning an existing one from version control?
13. Observe the below code snippet and choose correct options:
```tf
resource "local_file" "games" {
  file     = "/root/favorite-games"
  content  = "FIFA 21"
}
```
14. What does the "terraform show" command use to provide details of the Infrastructure?
15. You have been working on a terraform configuration file. When you run terraform plan, you see an output as shown below that states that the resource "local_file.pet must be replaced". What is the cause for this?
```tf
# local_file.pet must be replaced
-/+ resource "local_file" "pet" {
        content              = "We love pets!"
        directory_permission = "0777"
      ~ file_permission      = "0777" -> "0700" # forces replacement
        filename             = "/root/pet.txt"
      ~ id                   = "5f8fb950ac60f7f23ef968097cda0a1fd3c11bdf" -> (known after apply)
    }
```
16. What does “IaC” stand for?
17. Upon running "terraform init" within a configuration directory, you see an output as shown below. What is the provider and version that was initialized?
```tf
Initializing the backend...

Initializing provider plugins...
- Finding latest version of hashicorp/local...
- Installing hashicorp/local v1.4.0...
- Installed hashicorp/local v1.4.0 (signed by HashiCorp)

The following providers do not have any version constraints in configuration,
so the latest version was installed.

To prevent automatic upgrades to new major versions that may contain breaking
changes, we recommend adding version constraints in a required_providers block
in your configuration, with the constraint strings suggested below.

* hashicorp/local: version = "~> 1.4.0"

Terraform has been successfully initialized!
```
17. What allows Terraform to make use of a declarative approach?
18. Which of the following statements is true?




















