import { readFile, writeFile, mkdir } from 'node:fs/promises'
import path from 'node:path'

async function build() {
  const rootDir = process.cwd()
  const masterJson = JSON.parse(await readFile(path.join(rootDir, 'data/master_profile.json'), 'utf8'))
  const frHtml = await readFile(path.join(rootDir, 'index.html'), 'utf8')

  const languages = ['en', 'es', 'it']

  for (const lang of languages) {
    const loc = masterJson.locales[lang]
    if (!loc) continue

    const dir = path.join(rootDir, lang)
    await mkdir(dir, { recursive: true })

    let pageHtml = frHtml
      .replace('<html lang="fr">', `<html lang="${lang}">`)
      .replace(/<title>.*?<\/title>/, `<title>${loc.title}</title>`)
      .replace(/href="assets\//g, 'href="../assets/')
      .replace(/src="assets\//g, 'src="../assets/')
      .replace(/href="favicon\.ico"/g, 'href="../favicon.ico"')
      .replace(/src="video\//g, 'src="../video/')
      .replace(/src="storyboard\//g, 'src="../storyboard/')
      .replace(/href="index\.html"/g, 'href="../index.html"')
      .replace(/href="en\/index\.html"/g, 'href="index.html"')
      .replace(/href="es\/index\.html"/g, 'href="../es/index.html"')
      .replace(/href="it\/index\.html"/g, 'href="../it/index.html"')

    // Active class replacement for lang selector
    pageHtml = pageHtml
      .replace('<a href="index.html" class="is-active">FR</a>', '<a href="../index.html">FR</a>')
      .replace(`href="${lang === 'en' ? 'index.html' : '../' + lang + '/index.html'}"`, `href="index.html" class="is-active"`)

    // Hero headline and lede replacements
    pageHtml = pageHtml
      .replace('<p class="eyebrow">Concepteur-Rédacteur Senior · Films & Images</p>', `<p class="eyebrow">${loc.role}</p>`)
      .replace('<h1>Narration visuelle & <em>formats 360°</em></h1>', `<h1>${loc.headline}</h1>`)

    await writeFile(path.join(dir, 'index.html'), pageHtml, 'utf8')
    print(`Generated ${lang}/index.html successfully.`)
  }
}

function print(msg) {
  console.log('[build_pages]', msg)
}

build().catch(console.error)
