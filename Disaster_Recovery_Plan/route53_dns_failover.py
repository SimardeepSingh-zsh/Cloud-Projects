import boto3

# Initialize the Route 53 client
client = boto3.client('route53')

# Create primary and secondary health checks
primary_health_check = client.create_health_check(
    CallerReference='my-health-check-primary',
    HealthCheckConfig={
        'Type': 'HTTP',
        'ResourcePath': '/',
        'FullyQualifiedDomainName': 'primary.example.com',
        'RequestInterval': 30,
        'FailureThreshold': 3,
    }
)

secondary_health_check = client.create_health_check(
    CallerReference='my-health-check-secondary',
    HealthCheckConfig={
        'Type': 'HTTP',
        'ResourcePath': '/',
        'FullyQualifiedDomainName': 'secondary.example.com',
        'RequestInterval': 30,
        'FailureThreshold': 3,
    }
)

# Create a failover routing policy
response = client.create_traffic_policy(
    Name='failover-policy',
    Document='{"Comment":"Failover policy","Version":"2016-04-01","Statement":[{"Action":"failover","Resource":"/hostedzone/YOUR_PRIMARY_ZONE_ID","SetDNSName":{"Type":"A","Name":"primary.example.com","TTL":60}},{"Action":"failover","Resource":"/hostedzone/YOUR_SECONDARY_ZONE_ID","SetDNSName":{"Type":"A","Name":"secondary.example.com","TTL":60}}]}'
)

# Associate health checks with the routing policy
response = client.create_traffic_policy_instance(
    HostedZoneId='YOUR_PRIMARY_ZONE_ID',
    Name='primary.example.com',
    TTL=60,
    TrafficPolicyId='YOUR_FAILOVER_POLICY_ID'
)

response = client.create_traffic_policy_instance(
    HostedZoneId='YOUR_SECONDARY_ZONE_ID',
    Name='secondary.example.com',
    TTL=60,
    TrafficPolicyId='YOUR_FAILOVER_POLICY_ID'
)
