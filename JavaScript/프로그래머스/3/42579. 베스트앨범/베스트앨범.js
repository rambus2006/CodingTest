function solution(genres, plays) {
    // 1. 장르별 총 재생 횟수 계산
    const genrePlayCount = new Map();
    // 2. 장르별 곡 목록 작성
    const genreSongs = new Map();
    
    for (let i = 0; i < genres.length; i++) {
        const genre = genres[i];
        const play = plays[i];
        
        genrePlayCount.set(genre, (genrePlayCount.get(genre) || 0) + play);
        
        if (!genreSongs.has(genre)) {
            genreSongs.set(genre, []);
        }
        genreSongs.get(genre).push([i, play]);
    }
    
    // 3. 장르별 곡 정렬
    genreSongs.forEach((songs, genre) => {
        songs.sort((a, b) => {
            if (b[1] === a[1]) return a[0] - b[0]; // 재생 횟수가 같으면 고유 번호로 정렬
            return b[1] - a[1]; // 재생 횟수로 내림차순 정렬
        });
    });
    
    // 4. 장르별로 상위 두 곡 선택
    const bestAlbum = [];
    Array.from(genrePlayCount.entries())
        .sort((a, b) => b[1] - a[1]) // 총 재생 횟수로 장르 정렬
        .forEach(([genre]) => {
            const songs = genreSongs.get(genre);
            bestAlbum.push(songs[0][0]); // 상위 곡 추가
            if (songs.length > 1) bestAlbum.push(songs[1][0]); // 두 번째 곡 추가
        });
    
    // 5. 결과 반환
    return bestAlbum;
}
