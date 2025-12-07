---
vc-id: a7904000-848e-4946-952b-191dedaf843f
---
```dataviewjs
//--------------------------------------------------
// CONFIG
//--------------------------------------------------
const TARGET_FOLDER = "Chapter 7 - Equipment";  
const TARGET_TAG = "smallArms";   // e.g. "weapon"
const IGNORE_TAG = "increment";

//--------------------------------------------------
// 1. Collect all matching pages (folder + tag)
//--------------------------------------------------
let pages = dv.pages()
    .where(p => p.file.folder.includes(TARGET_FOLDER))
    .where(p => p.file.tags && p.file.tags.includes("#" + TARGET_TAG) && !p.file.tags.includes("#" + IGNORE_TAG));

//--------------------------------------------------
// 2. Merge helper (parent overrides child, child wins)
//--------------------------------------------------
function merged(a, b) {
    return Object.assign({}, a ?? {}, b ?? {});
}

//--------------------------------------------------
// 3. Group pages by parent
//--------------------------------------------------
let groups = new Map();

for (let p of pages) {

    // Resolve parent if extends: exists
    let parentPage = null;

    if (p.extends) {
        parentPage = dv.page(p.extends.path ?? p.extends);
    }

    // Key used for grouping (parent name or "(No Parent)")
    let parentKey = parentPage?.file?.name ?? "(No Parent)";

    // Create group if missing
    if (!groups.has(parentKey)) groups.set(parentKey, []);

    // Merge parent + child
    let data = merged(parentPage, p);

    // Extract your chosen fields
    let name = data.name ?? "";
    let caliber = data.caliber ?? "";
    let recoil = data.recoil ?? "";
    let notes = data.notes ?? "";
    let alias = data.aliases ?? "";

    // Add to the correct parent group
    groups.get(parentKey).push([
        p.file.link,
        name,
        alias,
        caliber,
        recoil,
        notes
    ]);
}

//--------------------------------------------------
// 4. Render grouped tables
//--------------------------------------------------
for (let [parentName, children] of groups) {
    children.sort((a, b) => a[1].localeCompare(b[1]));
    dv.header(3, parentName);
    dv.table(["File", "Name", "Aliases", "Caliber", "Recoil","Notes"], children);
}
```

