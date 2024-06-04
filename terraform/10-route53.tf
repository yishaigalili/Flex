data "aws_route53_zone" "primary" {
  name = "yishai-galili.com"
  private_zone = false
}

resource "aws_route53_record" "www" {
  zone_id = data.aws_route53_zone.primary.zone_id
  name    = "yishai-galili.com"
  type    = "A"

  alias {
    name                   = aws_lb.flex_app_alb.dns_name
    zone_id                = aws_lb.flex_app_alb.zone_id
    evaluate_target_health = true
  }
}