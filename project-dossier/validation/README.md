# Validation

A passing structural check proves only its stated scope. It does not prove
business, legal, privacy, security, accessibility, operational, or production
readiness.

Project-specific commands are authoritative in `.agent/validators.json`.
Current ordered sequence:

```text
/Users/jamesryancooper/.pyenv/versions/3.14.0/bin/python3 -B standalone-capability-family-packet-v1/scripts/validate-packet.py
python3 -B .agent/scripts/validate.py --check
python3 -B -m unittest discover -s .agent/tests -p 'test_*.py'
/Users/jamesryancooper/.pyenv/versions/3.14.0/bin/python3 -B standalone-capability-family-packet-v1/scripts/validate-packet.py --refresh-projections --write-manifest --refresh-checksums
/Users/jamesryancooper/.pyenv/versions/3.14.0/bin/python3 -B standalone-capability-family-packet-v1/scripts/validate-packet.py
python3 -B .agent/scripts/refresh.py --refresh
python3 -B .agent/scripts/validate.py --check
```

The first three commands are read-only. The two refresh commands are explicit
writers and must wait until source freeze. No command authorizes dependency
installation. The host-specific packet runtime is an acknowledged portability
limitation.

`EVD-0001` records the adoption inventory, runtime observations, and
identity-source comparison. `EVD-0002` records the final local packet,
harness, mutation, and integrity validation. `EVD-0003` records exact private
creation, foundation publication, first-push equality, and the closure
commit's direct-verification boundary.
