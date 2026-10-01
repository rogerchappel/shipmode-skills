"""Build a deterministic source ZIP; omit Git, cache, dist and local metadata."""
from pathlib import Path
import hashlib
import zipfile

ROOT = Path(__file__).resolve().parents[1]
version = (ROOT / 'VERSION').read_text().strip()
out = ROOT / 'dist'
out.mkdir(exist_ok=True)
archive = out / f'shipmode-skills-{version}.zip'
files = sorted(p for p in ROOT.rglob('*') if p.is_file() and not any(part in {'.git', 'dist', '__pycache__'} for part in p.relative_to(ROOT).parts) and p.suffix != '.pyc')
with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED) as z:
    for p in files:
        info = zipfile.ZipInfo('shipmode-skills/' + p.relative_to(ROOT).as_posix(), (2026, 10, 2, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o100644 << 16
        z.writestr(info, p.read_bytes())
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    assert len(z.namelist()) == len(files)
    for p in files:
        assert z.read('shipmode-skills/' + p.relative_to(ROOT).as_posix()) == p.read_bytes()
checksum = hashlib.sha256(archive.read_bytes()).hexdigest()
(archive.with_suffix('.zip.sha256')).write_text(f'{checksum}  {archive.name}\n')
print(f'{archive}: {len(files)} files; verified every archived byte; SHA-256 {checksum}')
