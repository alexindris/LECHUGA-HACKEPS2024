import 'package:flutter/material.dart';

class SampleItemDetailsView extends StatelessWidget {
  static const routeName = '/item-details';

  const SampleItemDetailsView({super.key});

  @override
  Widget build(BuildContext context) {
    final parking =
        ModalRoute.of(context)?.settings.arguments as Map<String, dynamic>;

    return Scaffold(
      appBar: AppBar(
        title: Image.asset(
          Theme.of(context).brightness == Brightness.dark
              ? 'assets/images/app_logo_inverted.png'
              : 'assets/images/app_logo.png',
          height: 40,
        ),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Center(
              child: Text(
                parking['name'],
                style: Theme.of(context)
                    .textTheme
                    .bodyMedium
                    ?.copyWith(fontSize: 40, fontWeight: FontWeight.bold),
                textAlign: TextAlign.center,
              ),
            ),
            Container(
              margin: const EdgeInsets.only(top: 16),
              width: double.infinity,
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(39),
                color:
                    Theme.of(context).floatingActionButtonTheme.backgroundColor,
              ),
              child: Padding(
                padding: const EdgeInsets.all(16),
                child: Column(children: [
                  Padding(
                    padding: const EdgeInsets.only(top: 16.0),
                    child: Text(
                      'Number of free lots',
                      style: Theme.of(context).textTheme.bodyMedium?.copyWith(
                            fontSize: 30,
                            color: Theme.of(context).primaryColor,
                          ),
                    ),
                  ),
                  Container(
                    margin: const EdgeInsets.only(top: 16),
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(20),
                      color: Theme.of(context).primaryColor,
                    ),
                    child: Text(
                        '   ${parking['totalLots'] - parking['occupiedLots']}/${parking['totalLots']}   ',
                        style: Theme.of(context).textTheme.bodyMedium?.copyWith(
                              fontSize: 40,
                              fontWeight: FontWeight.bold,
                            )),
                  ),
                  Padding(
                    padding: const EdgeInsets.only(top: 16.0),
                    child: Text(
                      parking['address'],
                      style: Theme.of(context).textTheme.bodyMedium?.copyWith(
                            fontSize: 20,
                            color: Theme.of(context).primaryColor,
                          ),
                      textAlign: TextAlign.center,
                    ),
                  ),
                ]),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
