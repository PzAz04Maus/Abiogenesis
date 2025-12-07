---
vc-id: a7904000-848e-4946-952b-191dedaf843f
obsidianUIMode: preview
---
```dataviewjs
//--------------------------------------------------
// CONFIG
//--------------------------------------------------
const TARGET_FOLDER = "Chapter 7 - Equipment/Small arms Operating System";  
const INCLUDE_TAGS = ["smallArms","candidate"];   // e.g. "weapon"
const EXCLUDE_TAGS = ["increment"];

//--------------------------------------------------
// 1. Collect all matching pages (folder + tag)
//--------------------------------------------------
let pages = dv.pages()
	.where(p => p.file.folder.includes(TARGET_FOLDER))
    .where(p => INCLUDE_TAGS.every(t => p.file.etags?.includes("#" + t)))
    .where(p => !EXCLUDE_TAGS.every(t => p.file.etags?.includes("#" + t)));
    
    //.where(p => p.file.tags && p.file.tags.includes("#" + TARGET_TAG) && !p.file.tags.includes("#" + IGNORE_TAG));

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
    //let name = data.name ?? "";
    let type = data.type ?? "";
    let caliber = data.caliber ?? "";
    let recoil = data.recoil ?? "";
    let notes = data.notes ?? "";
    let alias = data.aliases ?? "";

    // Add to the correct parent group
    groups.get(parentKey).push([
        p.file.link,
        type,
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
	children.sort((a, b) =>
    String(a[1] ?? "").localeCompare(String(b[1] ?? ""))
	);
    dv.header(3, parentName);
    dv.table(["File", "Family", "Aliases", "Caliber", "Recoil","Notes"], children);
}
```

