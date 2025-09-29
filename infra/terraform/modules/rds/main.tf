resource "aws_db_subnet_group" "this" {
  name       = "${var.project}-rds-subnet"
  subnet_ids = var.subnet_ids
  tags       = var.tags
}

resource "aws_security_group" "rds" {
  name        = "${var.project}-rds-sg"
  description = "RDS access"
  vpc_id      = var.vpc_id

  ingress {
    description      = "App access"
    from_port        = var.port
    to_port          = var.port
    protocol         = "tcp"
    security_groups  = var.allowed_security_groups
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = var.tags
}

resource "aws_db_instance" "this" {
  identifier              = "${var.project}-postgres"
  engine                  = "postgres"
  engine_version          = var.engine_version
  instance_class          = var.instance_class
  allocated_storage       = var.allocated_storage
  username                = var.username
  password                = var.password
  db_name                 = var.database_name
  port                    = var.port
  publicly_accessible     = false
  storage_encrypted       = true
  skip_final_snapshot     = true
  db_subnet_group_name    = aws_db_subnet_group.this.name
  vpc_security_group_ids  = [aws_security_group.rds.id]
  backup_retention_period = 7
  maintenance_window      = "Mon:00:00-Mon:03:00"
  deletion_protection     = false
  tags                    = var.tags
}
