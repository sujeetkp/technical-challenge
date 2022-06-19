locals {
  prefix = var.db_server_name_prefix
  db_server_name = "${local.prefix}-${var.environment}-${var.department}-${random_string.random.id}"
  tags = {
    department = var.department
    environment = var.environment
  }
}