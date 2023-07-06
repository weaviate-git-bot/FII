<html>
    <head>
        <title>${title}</title>
    </head>
    <body>
        <h1>${title}</h1>
        <ul>
        <#list items as item>
            <li>
                <h3>${item.title}</h3>
                <p>Can be found at: ${item.location}</p>
                <p>Written by: ${item.author}</p>
            </li>
        </#list>
        </ul>
    </body>
</html>