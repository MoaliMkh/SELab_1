# آزمایش اول: Git
## اجرای برنامه
این برنامه یک پیام‌رسان با دستورات command line را پیاده‌سازی کرده است. ابتدا باید server.py را اجرا کرده و پس از آن به ازای هر تعداد کاربر دلخواه یک بار client.py اجرا شود.
## دستورات
کاربر می‌تواند از دستورات زیر برای ارتباط با برنامه استفاده نماید:

+ دستور `<signup <username> <password`
  + یک کاربر جدید به سامانه اضافه می‌کند. نام کاربری تکراری به کاربر خطای مناسب را نمایش خواهد داد.
+ دستور `<login <username> <password`
  + کاربر به کمک این دستور می‌تواند وارد سامانه شود.
+ دستور `<signup <username> <password`
  + یک پیام دلخواه به یکی از کاربرهای سامانه ارسال کند. در صورتی که کاربر مورد نظر یافت نشود؛ خطای مناسب نمایش داده خواهد شد.
+ دستور `online`
  + کاربران حاضر در سیستم را نمایش می‌دهد.
+ دستور `inbox`
  + پیام‌های سایر کاربران به کاربر فعلی را نمایش می‌دهد.
+ دستور `<new_group <group name`
  + یک گروه با نام دلخواه ایجاد می‌نماید. در صورت انتخاب نام تکراری، خطای مناسب نمایش داده خواهد شد.
+ دستور `exit`
  + کاربر را از سامانه خارج کرده و برنامه او را terminate می‌کند.
## پاسخ پرسش‌ها
+ **پوشه‌ی .git** چیست؟ چه اطلاعاتی در آن ذخیره می‌شود؟ با چه دستوری ساخته می‌شود؟
  + در این پوشه metadata های مورد نیاز ذخیره می‌شود. به عنوان مثال اطلاعات مربوط به تاریخچه commit ها و یا تغییرات اعمال شده در هر یک از شاخه‌ها و یا برچسب‌ها (tag) و سایر اطلاعات مربوط به مخزن پروژه در این پوشه نگهداری می‌گردد.
  ([wikipedia](/https://en.wikipedia.org/wiki/Git))
  + هنگامی که یک پروژه با دستور `git clone` بر روی local آورده می‌شود و یا از ابتدا به کمک دستور `git init` مخزن local ایجاد می‌گردد؛ این پوشه به شکل خودکار ظاهر خواهد شد.
+ منظور از **atomic** بودن در atomic commit و atomic pull-request چیست؟
  + منظور از atomic commit کوچک بودن اندازه تغییرات در هر commit تا حد امکان است. بنابراین هر commit نشان‌دهنده یک تغییر کوچک و cohesive در سطح پروژه خواهد بود.
  + منظور از atomic pull request کمینه و یکپارچه بودن commit های موجود در هر PR است. بنابراین در هر PR تعدادی atomic commit برای تحقق یک feature مشخص و یا رفع یک مسئله خاص وجود دارد که نباید با سایر بخش‌ها coupled باشد.
+ تفاوت دستورهای **fetch** و **pull** و **merge** و **rebase** را بیان کنید.
  + دستور `fetch` تمام اشیاء، commit ها و ارجاعات موجود در یک مخزن را بارگیری کرده و به مخزن محلی یا همان local repository اضافه می‌نماید.
([javapoint](https://www.javatpoint.com/git-fetch))
  + دستور `pull` اطلاعات و محتویات یک مخزن دیگر و یا local branch را گرفته و تغییرات فعلی یکپارچه می‌سازد. نحوه استفاده از این دستور نیز به شکل `git pull [<options>] [<repository> [<refspec>…​]]` می‌باشد.
([git-scm](https://git-scm.com/docs/git-pull))
  + دستور `merge` تغییرات دو یا چند شاخه را با یکدیگر ادغام کرده و اشاره‌گر HEAD را بر روی commit نهایی مشترک آنها قرار می‌دهد. نحوه استفاده از این دستور به شکل `git merge [<name of the branch to be merged>]` است.
([geeksforgeeks](https://www.geeksforgeeks.org/git-merge/))
  + دستور `rebase` نیز مشابه دستور `merge` برای یکپارچه‌سازی تغییرات استفاده می‌شود. به کمک این دستور می‌توان HEAD یک شاخه دلخواه را بر روی درخت تغییرات جابجا کرد. به عنوان مثال فرض کنید یک شاخه experiment از main جدا شده و دارای چند commit است. اگر شاخه experiment بر روی شاخه اصلی rebase شود؛ در واقع تمام تغییرات آن در ادامه شاخه main اضافه می‌شود؛ البته اعمال این تغییرات باید به ترتیب باشد. تصویر زیر نمایی از این دستور را نمایش می‌دهد:
![image](https://github.com/MoaliMkh/SELab_1/assets/59196723/16f29eca-d3cc-4757-929f-243c3e117d55)

([git-scm](https://git-scm.com/book/en/v2/Git-Branching-Rebasing))

+ تفاوت سه دستور **reset** و **revert** و **restore** را بیان کنید.
  + دستور `reset` برای برگرداندن تغییرات یک commited file است. پس از استفاده از این دستور وضعیت فایل به حالت پیش از تغییرات بازخواهد گشت.
  ([w3schools](https://www.w3schools.com/git/git_reset.asp?remote=github))
  + دستور `revert` یکی از ویژگی‌های اصلی git را نمایش می‌دهد. به کمک این دستور می‌توان بین نسخه‌ها یا همان commit های مختلف جابجا شد و وضعیت پروژه در آن نسخه را مشاهده کرد.
  + دستور `restore` نیز برای برگرداندن تغییرات یک یا چند فایل در commit های قبلی است. ولی تفاوت آن با دستور `reset` در عدم تغییر تاریخچه commit ها است.
+ منظور از **stage** چیست؟ دستور **stash** چه کاری را انجام می‌دهد؟
  + در git باید file هایی که تغییر می‌کنند به روی سکوی stage بیایند تا از آنجا به سمت commit پرتاپ شوند!
  + در واقع stage وضعیتی است فایل‌هایی که تغییرات آنها در commit فعلی ذخیره می‌شود؛ در آن قرار گرفته و پس از commit شدن به حالت unmodified برمی‌گردند.
  + دستور `stash` برای ذخیره تغییرات استفاده می‌شود؛ اما در شرایطی که تمایلی به ذخیره تغییرات به عنوان یک commit وجود ندارد. مثلا در شرایطی که قرار است `checkout branch` انجام شود و هنوز تغییرات فعلی به مرحله پایداری نرسیده است؛ می‌توان از این دستور استفاده کرد تا جابجایی بین شاخه‌ها بدون مشکل انجام شود. به کمک دستور `git stash pop` می‌توان این تغییرات را بازیابی کرد.
([javapoint](https://www.javatpoint.com/git-stash))
+ مفهوم **snapshot** به چه معناست؟
  + برخی از version control system ها تغییرات هر نسخه نسبت به نسخه قبل را ذخیره می‌کنند. اما git وضعیت کامل پروژه را در هر commit نگهداری می‌نماید. هر کدام از این وضعیت‌ها یک snapshot نام دارد که در آن حالت فعلی tracked file ها ذخیره شده است.
  ([stack overflow](https://stackoverflow.com/questions/4964099/what-is-a-git-snapshot#:~:text=A%20snapshot%20is%20a%20representation,first%20moment%20it%20was%20tracked.))

## چشم‌انداز
در نسخه‌های بعدی امکان اضافه کردن عضو به گروه و ارسال پیام گروه به وجود خواهد آمد.
