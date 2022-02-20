import pickle

data = pickle.load(open('ethdenver_repo_contributors.pk', 'rb'))

for repo in data:
    print('URL: https://github.com/'+repo['full_name'])
    print('Overall contributor score:', repo['score'])
    if repo['score'] == 0:
        print('No scores found for contributors')
    else:
        print('Cnntributors:')
        for contributor in repo['contributors']:
            print('\t', contributor['login'])
            if 'assessment' not in contributor:
                print('\t\t no scores found')
            else:
                for skill in contributor['assessment']['skills']:
                    if skill['score'] > 0:
                        print('\t\t', skill['name'], 'score:', skill['score'], 'average:', skill['average'])
    print('-'*30)